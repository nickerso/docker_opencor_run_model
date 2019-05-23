import sys
import json

import OpenCOR as oc


# ./OpenCOR-2019-05-18-Linux/bin/OpenCOR -c PythonRunScript::script run_model.py 7
def main(stimulus_period):
    s = oc.openSimulation('/home/opencor/models/noble_varghese_kohl_noble_1998_a.cellml')

    d = s.data()

    # Set integration range
    d.setPointInterval(0.1)
    d.setEndingPoint(100000)

    # print('Setting stimulus period to:', stimulus_period)
    c = d.constants()
    c['membrane/stim_period'] = stimulus_period

    # Run the simulation
    s.run()

    r = s.results()

    json_format = json.dumps({'membrane': {'V': r.states()['membrane/V'].values().tolist()}})
    print(json_format)


if __name__ == "__main__":
    args = sys.argv
    args.pop(0)  # Script name.
    try:
        period = float(args.pop(0))
    except ValueError:
        print("Usage: docker run hsorby/opencor-python <float>")
        print("  where <float> is the stimulation period as a decimal number.")
        sys.exit(2)

    main(period)
