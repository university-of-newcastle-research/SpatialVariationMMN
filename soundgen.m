freqs = [300, 600, 1000];
durs = [50, 100];  % In ms
delays = [.2, .37, .5, .55]; % In ms,	+ 0 as well
degrees = [22.5, 45, 67, 90]; % To match delays above
ears = ["left", "right"];

for d = 1:size(durs,2)
    % 0 degree version version
    component_specs = {};
    for f = 1:size(freqs,2)
        ss = PsySound.SoundSpec();
        ss.Ramp_length_start = 5*10^-4;
        ss.Ramp_length_end = 5*10^-4;
        ss.Duration=durs(d)/1000;
        ss.Sample_frequency=48000;
        ss.Frequency=freqs(f);
        component_specs{end+1} = ss;
    end

    cs = PsySound.Sound(component_specs{1});
    for c = 2:size(component_specs,2)
        cs = cs.combine(PsySound.Sound(component_specs{c}));
    end
    cs.Filename = strcat('Central', "_", int2str(durs(d)), 'ms.wav');
    cs.Save();

	for e = 1:size(ears,2)
		for t = 1:size(delays,2)
			component_specs{1}.Ear = ears(e);
			component_specs{1}.Delay = delays(t)*10^-3;
			component_specs{1}.Type = 'time';
			cs = PsySound.Sound(component_specs{1});
			for c = 2:size(component_specs,2)
				component_specs{c}.Ear = ears(e);
				component_specs{c}.Delay = delays(t)*10^-3;
				component_specs{c}.Type = 'time';
				cs = cs.combine(PsySound.Sound(component_specs{c}));
			end
			cs.Filename = strcat(ears(3-e), "_", num2str(degrees(t)), "deg_", int2str(durs(d)), 'ms.wav');
			cs.Save();
		end
	end
end
