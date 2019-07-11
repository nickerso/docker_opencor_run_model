import sys
import json

import OpenCOR


def main(stimulation_mode, stimulation_level):
    rc = 3
    #s = OpenCOR.openSimulation('/home/opencor/models/action-potential.xml')
    s = OpenCOR.openSimulation('/home/opencor/models/HumanSAN_Fabbri_Fantini_Wilders_Severi_2017.sedml')

    d = s.data()

    # Set integration range
    d.setPointInterval(0.01)  # s
    d.setEndingPoint(10)  # s

    #print('Setting stimulation mode to:', stimulation_mode)
    #print('Setting stimulation level to:', stimulation_level)
    c = d.constants()
    c['Rate_modulation_experiments/Iso_1_uM'] = 1.0  # dimensionless
    if stimulation_mode == 1:
        # Stellate stimulation 0 - 1 :: 22 - 0
        c['Rate_modulation_experiments/ACh'] = (1.0-stimulation_level) * 22.0e-6
    else:
        # Vagus stimulation 0 - 1 :: 22 - 38
        c['Rate_modulation_experiments/ACh'] = 22.0e-6 + stimulation_level * (38.0e-6 - 22.0e-6)


    # Run the simulation
    try:
        if s.run():
            r = s.results()

            json_format = json.dumps({'membrane': {'v': r.algebraic()['Membrane/V'].values().tolist()}})
            print(json_format)
            rc = 0
        else:
            rc = 4
    except RuntimeError:
        rc = 5

    return rc


if __name__ == "__main__":
    args = sys.argv
    args.pop(0)  # Script name.
    stimulation_mode = 1
    stimulation_level = 0.0
    try:
        stimulation_mode = int(args.pop(0))
        stimulation_level = float(args.pop(0))
    except ValueError:
        print("Usage: docker run hsorby/opencor-python <int> <float>")
        print("  where <int> is the stimulation mode as an integer number (1:stellate; 2:vagal).")
        print("  where <float> is the stimulation level (0-1) as a decimal number.")
        sys.exit(2)

    rc = main(stimulation_mode, stimulation_level)
    sys.exit(rc)

