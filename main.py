import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("data.xlsx")
data = data.set_index("DEPTID")

data['BONUS'] = data['BONUS'].map({"Yes": 1, "No": 0})
print(data)

fig, axs = plt.subplots(4,1)
axs[0].plot(data.index, data ['NAME'])
axs[0].set_title("Random Data")
axs[0].set_xlabel("DEPTID")


plt.plot(data.index, data ['NAME'])
plt.xlabel("DEPTID")
plt.ylabel("NAME")
plt.show