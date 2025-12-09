import numpy as np
np.set_printoptions(suppress=True)

def load_dataset():
    data = np.genfromtxt("../data/vgsales.csv", dtype=str, delimiter=",", skip_header=1, invalid_raise=False, filling_values="", missing_values="") 
    names = data[:, 1]
    platforms = data[:, 2]
    years = np.array([int(x) if x != 'N/A' else np.nan for x in data[:, 3]]) 
    genres=data[:, 4]
    publishers=data[:, 5]
    na_sales=np.array([float(x) if x != 'N/A' else np.nan for x in data[:, 6]]) 
    eu_sales=np.array([float(x) if x != 'N/A' else np.nan for x in data[:, 7]]) 
    jp_sales=np.array([float(x) if x != 'N/A' else np.nan for x in data[:, 8]]) 
    other_sales=np.array([float(x) if x != 'N/A' else np.nan for x in data[:, 9]]) 
    global_sales=np.array([float(x) if x != 'N/A' else np.nan for x in data[:, 10]]) 

    return names, platforms, years, genres, publishers, na_sales, eu_sales, jp_sales, other_sales, global_sales