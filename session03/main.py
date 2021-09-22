import numpy as np
from numpy import ogrid
import pandas as pd

arr = np.array([7, 3, 5, 2.5])
# arr2 = np.array(7)
print(arr[3])
print(arr.shape)
print(arr.size)
print(list(arr))
print(arr.tolist())
print([*arr])
# print(type(arr[3]))
# print(arr.shape)
print(arr + 3)
print(arr > 3)
print(arr[::-1])
print(np.flip(np.array([[1, 2], [2, 3], [4, 5]])))
print(np.array([[1, 2], [2, 3], [4, 5]]).flatten())
print(np.array([[1, 2], [2, 3], [4, 5]]).reshape(1, 6))
print(np.array([[1, 2], [2, 3], [4, 5]]).ravel())
print(np.array(range(1, 5)))
print(np.full([2, 2], 7))
print(np.arange(1, 10, 2))
print(ogrid[0:5])
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(df["Name"].values)

ps = pd.Series([1, 2, 3], index=["a", "b", "c"])
print(ps)
ps["A"] = 4
ps[3] = 9
print(ps)
s2 = pd.Series({"name": "khalid"})
print(df[["Name", "Age"]])
print("++++")
print(df.where(df.Age > 22))
print(df[df.Age > 22])
print(type(df.Age))
