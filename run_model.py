import sys
import json

import OpenCOR as oc


# ./OpenCOR-2019-05-18-Linux/bin/OpenCOR -c PythonRunScript::script run_model.py 7
def main(stimulus_period):
    s = oc.openSimulation('/home/opencor/models/action-potential.xml')

    d = s.data()

    # Set integration range
    d.setPointInterval(10) #ms
    d.setEndingPoint(100000) #ms

    # print('Setting stimulus period to:', stimulus_period)
    c = d.constants()
    c['membrane/period'] = stimulus_period #ms

    # Run the simulation
    s.run()

    r = s.results()

    json_format = json.dumps({'membrane': {'v': r.states()['membrane/v'].values().tolist()}})
    print(json_format)


if __name__ == "__main__":
    args = sys.argv
    args.pop(0)  # Script name.
    try:
        period = float(args.pop(0))
    except ValueError:
        print("Usage: docker run hsorby/opencor-python <float>")
        print("  where <float> is the stimulation period in milliseconds as a decimal number.")
        sys.exit(2)

    main(period)
