import sys
import json
from scipy.signal import find_peaks

import opencor


def main(stimulation_mode_parameter, stimulation_level_parameter):
    return_code = 0
    s = opencor.open_simulation('/home/opencor/models/HumanSAN_Fabbri_Fantini_Wilders_Severi_2017.sedml')
    d = s.data()
    c = d.constants()
    stimulation_level_parameter = max(0.0, min(1.0, stimulation_level_parameter))

    c['Rate_modulation_experiments/Iso_1_uM'] = 1.0  # dimensionless
    if stimulation_mode_parameter == 1:
        # Stellate stimulation 0 - 1 :: 22 - 0
        c['Rate_modulation_experiments/ACh'] = (1.0 - stimulation_level_parameter) * 22.0e-6
    elif stimulation_mode_parameter == 2:
        # Vagus stimulation 0 - 1 :: 22 - 38
        c['Rate_modulation_experiments/ACh'] = 22.0e-6 + stimulation_level_parameter * (38.0e-6 - 22.0e-6)
    else:
        return_code = 4

    # Run the simulation
    try:
        if return_code == 0 and s.run():
            r = s.results()
            output_data = {'membrane': {'v': r.algebraic()['Membrane/V'].values().tolist()}}
            peaks = find_peaks(output_data['membrane']['v'])[0]
            output_data['heart_rate'] = len(peaks)
            json_format = json.dumps(output_data)
            print(json_format)
        else:
            return_code = 5
    except RuntimeError:
        return_code = 6

    return return_code


def usage():
    print("Usage: docker run hsorby/opencor-python <int> <float>")
    print("  where <int> is the stimulation mode as an integer number (1:stellate; 2:vagal).")
    print("  where <float> is the stimulation level (0-1) as a decimal number.")


if __name__ == "__main__":
    args = sys.argv
    args.pop(0)  # Script name.
    stimulation_mode = 1
    stimulation_level = 0.0
    try:
        stimulation_mode = int(args.pop(0))
        stimulation_level = float(args.pop(0))
    except ValueError:
        usage()
        sys.exit(2)
    except IndexError:
        usage()
        sys.exit(2)

    rc = main(stimulation_mode, stimulation_level)
    sys.exit(rc)
