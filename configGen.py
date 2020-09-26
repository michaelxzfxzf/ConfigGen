import jinja2
import os

template_file = "spoke.j2"
csv_parameter_file = "parameters1.csv"
config_parameters = []
output_directory = "_output"

# 1. read the contents from the CSV files
print("Read CSV parameter file...")
f = open(csv_parameter_file)
csv_content = f.read()
f.close()

#2 . convert csv
print("Convert CSV file to dictionaries...")
csv_lines = csv_content.splitlines()
headers = csv_lines[0].split(",")
for i in range(1, len(csv_lines)):
    values = csv_lines[i].split(",")
    parameter_dict = dict()
    for h in range(0, len(headers)):
        parameter_dict[headers[h]] = values[h]
    config_parameters.append(parameter_dict)

# 3. load Jinja2
print("Create Jinja2 environment...")
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."))
template = env.get_template(template_file)


if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# 4. generate config
print("Create templates...")
for parameter in config_parameters:
    result = template.render(parameter)
    f = open(os.path.join(output_directory, parameter['siteName'] + ".config"), "w")
    f.write(result)
    f.close()
    print("Configuration '%s' created..." % (parameter['siteName'] + ".config"))
print("DONE")
