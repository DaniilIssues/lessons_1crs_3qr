import yaml

data = {
    1: [1, 2, 3, 4, 5, 6, 7],
    2: 2,
    3: {
        1: "1€",
        2: "2€",
        3: "3€",
        4: "4€",
    }
}

with open('file.yaml', 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml') as f_n:
    print(f_n.read())
