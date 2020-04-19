import os
import re
import pandas as pd

path_result = "output"
path_csv = "openmm_benchmark.csv"

list_system = ['QuadroRTX8000', 'TitanRTX']

list_precision = ['single', 'mixed', 'double']

list_test = {
    'CUDA_gbsa': ('CUDA_gbsa', "^.*ns/day.*$", -2),
    'CUDA_rf': ('CUDA_rf', "^.*ns/day.*$", -2),
    'CUDA_pme': ('CUDA_pme', "^.*ns/day.*$", -2),
    'CUDA_apoa1rf': ('CUDA_apoa1rf', "^.*ns/day.*$", -2),
    'CUDA_apoa1pme': ('CUDA_apoa1pme', "^.*ns/day.*$", -2),
    'CUDA_apoa1ljpme': ('CUDA_apoa1ljpme', "^.*ns/day.*$", -2),
    'CUDA_amoebagk': ('CUDA_amoebagk', "^.*ns/day.*$", -2),
    'CUDA_amoebapme': ('CUDA_amoebapme', "^.*ns/day.*$", -2),
    'OpenCL_gbsa': ('OpenCL_gbsa', "^.*ns/day.*$", -2),
    'OpenCL_rf': ('OpenCL_rf', "^.*ns/day.*$", -2),
    'OpenCL_pme': ('OpenCL_pme', "^.*ns/day.*$", -2),
    'OpenCL_apoa1rf': ('OpenCL_apoa1rf', "^.*ns/day.*$", -2),
    'OpenCL_apoa1pme': ('OpenCL_apoa1pme', "^.*ns/day.*$", -2),
    'OpenCL_apoa1ljpme': ('OpenCL_apoa1ljpme', "^.*ns/day.*$", -2),
    'OpenCL_amoebagk': ('OpenCL_amoebagk', "^.*ns/day.*$", -2),
    'OpenCL_amoebapme': ('OpenCL_amoebapme', "^.*ns/day.*$", -2)             
}

def gather(name, system, df, precision):
    column_name, key, pos = list_test[name]
    pattern = re.compile(key)

    filename = path_result + '/' + system + '/' + precision + "_" + name + '.txt'
    count = 0.000001

    if os.path.exists(filename):
        throughput = 0
        # Sift through all lines and only keep the last occurrence
        for i, line in enumerate(open(filename)):

            for match in re.finditer(pattern, line):
                try:
                    throughput = float(match.group().split(' ')[pos])
                except:
                    pass

        if throughput > 0:
            df.at[system, column_name] = round(throughput, 2)
        else:
            print(system + "/" + name + " " + filename + ": something wrong")
        
    else:
        df.at[system, column_name] = 0.0

def main():

    for precision in list_precision:
        columns = []
        for test_name, value in sorted(list_test.items()):
            columns.append(list_test[test_name][0])

        df = pd.DataFrame(index=list_system, columns=columns)
        df = df.fillna(-1.0)

        for system in list_system:
            for test_name, value in sorted(list_test.items()):
                gather(test_name, system, df, precision)

        df.index.name = 'name_gpu'

        df.to_csv(precision + '_' + path_csv)

if __name__ == "__main__":
    main()