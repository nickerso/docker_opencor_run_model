import sys
import json

import OpenCOR


def main(stimulus_period):
    rc = 3
    s = OpenCOR.openSimulation('/home/opencor/models/action-potential.xml')

    d = s.data()

    # Set integration range
    d.setPointInterval(10)  # ms
    d.setEndingPoint(100000)  # ms

    # print('Setting stimulus period to:', stimulus_period)
    c = d.constants()
    c['membrane/period'] = stimulus_period  # ms

    # Run the simulation
    try:
        if s.run():
            r = s.results()

            json_format = json.dumps({'membrane': {'v': r.states()['membrane/v'].values().tolist()}})
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
    try:
        period = float(args.pop(0))
    except ValueError:
        print("Usage: docker run hsorby/opencor-python <float>")
        print("  where <float> is the stimulation period in milliseconds as a decimal number.")
        sys.exit(2)

    rc = main(period)
    sys.exit(rc)

