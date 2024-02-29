color_cycles = {
    "matlab": [
        "#0072bd",
        "#d95319",
        "#edb120",
        "#7e2f8e",
        "#77ac30",
        "#4dbeee",
        "#a2142f",
    ],
    "python": [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ],
    "plotly": [
        "#636efa",
        "#ef553b",
        "#00cc96",
        "#ab63fa",
        "#ffa15a",
        "#19d3f3",
        "#ff6692",
        "#b6e880",
        "#ff97ff",
        "#fecb52",
    ],
    "whooie": [
        "#1f77b4",  # 0 blue
        "#d95319",  # 1 auburn
        "#edb120",  # 2 canary
        "#7e2f8e",  # 3 purple
        "#46add9",  # 4 cyan
        "#ff7f0e",  # 5 tangerine
        "#3d786e",  # 6 dark seafoam
        "#505050",  # 7 gray
        "#a2142f",  # 8 burgundy
        "#bf7878",  # 9 dark rose
    ]
}

color_scales = {
    "hot_cold": [
        (0.000, "#101010"),
        (0.100, "#3f119d"),
        (0.350, "#3967d0"),
        (0.500, "#f0f0f0"),
        (0.625, "#f1b931"),
        (1.000, "#dd0000"),
    ],
    "fire_ice": [
        (0.000, "#2165ac"),
        (0.167, "#68a9cf"),
        (0.333, "#d2e6f1"),
        (0.500, "#f8f8f8"),
        (0.667, "#ffdbc8"),
        (0.833, "#f08a62"),
        (1.000, "#b0172b"),
    ],
    "powerade": [
        (0.000, "#542689"),
        (0.167, "#9a8dc2"),
        (0.333, "#d9daec"),
        (0.500, "#f8f8f8"),
        (0.667, "#d2e6f1"),
        (0.833, "#68a9cf"),
        (1.000, "#2165ac"),
    ],
    "floral": [
        (0.000, "#35c9a5"),
        (0.167, "#5cbea7"),
        (0.333, "#80b4a8"),
        (0.500, "#a8a8a8"),
        (0.667, "#c2a1a8"),
        (0.833, "#e099a9"),
        (1.000, "#fd8fa8"),
    ],
    "plasma": [
        (0.000, "#000000"),
        (0.450, "#3b4568"),
        (0.600, "#586186"),
        (0.700, "#939cc4"),
        (1.000, "#f8f8f8"),
    ],
    "cyborg": [
        (0.000, "#101010"),
        (0.100, "#3967d0"),
        (1.000, "#dd0000"),
    ],
    "vibrant": [
        (0.000, "#101010"),
        (0.050, "#012d5e"),
        (0.125, "#0039a7"),
        (0.250, "#1647cf"),
        (0.375, "#6646ff"),
        (0.500, "#bc27ff"),
        (0.600, "#dc47af"),
        (0.800, "#f57548"),
        (0.900, "#f19e00"),
        (0.950, "#fbb800"),
        (1.000, "#fec800"),
    ],
    "artsy": [
        (0.000, "#1f0109"),
        (0.034, "#1f0110"),
        (0.069, "#230211"),
        (0.103, "#250816"),
        (0.138, "#270b1b"),
        (0.172, "#250f1d"),
        (0.207, "#251521"),
        (0.241, "#251a25"),
        (0.276, "#2c1b28"),
        (0.310, "#271d2b"),
        (0.345, "#24202d"),
        (0.379, "#232632"),
        (0.414, "#212d32"),
        (0.448, "#1e343c"),
        (0.483, "#173e44"),
        (0.517, "#17464a"),
        (0.552, "#104a49"),
        (0.586, "#0e5553"),
        (0.621, "#00635f"),
        (0.655, "#007065"),
        (0.690, "#007a6d"),
        (0.724, "#0e8476"),
        (0.759, "#1c8c7d"),
        (0.793, "#219581"),
        (0.828, "#2f9f8a"),
        (0.862, "#49a890"),
        (0.897, "#60b89d"),
        (0.931, "#7ec8a9"),
        (0.966, "#9ad6b4"),
        (1.000, "#bce6bf"),
    ],
    "pix": [
        (0.000, "#0d2b45"),
        (0.143, "#16334d"),
        (0.286, "#544e68"),
        (0.429, "#8d697a"),
        (0.571, "#d08159"),
        (0.714, "#ffaa5e"),
        (0.857, "#ffd4a3"),
        (1.000, "#ffecd6"),
    ],
    "sunset": [
        (0.000, '#0d0887'),
        (0.111, '#46039f'),
        (0.222, '#7201a8'),
        (0.333, '#9c179e'),
        (0.444, '#bd3786'),
        (0.555, '#d8576b'),
        (0.666, '#ed7953'),
        (0.777, '#fb9f3a'),
        (0.888, '#fdca26'),
        (1.000, '#f0f921'),
    ],
}

def opacity(i, N, m=0.2, p=2):
    return m + (1 - m) * (i / N)**p

def dot_dash(n):
    return n * [1, 1] + [8, 1]

class Slicer:
    def __init__(self):
        return

    def __getitem__(self, slice):
        return slice

S = Slicer()

