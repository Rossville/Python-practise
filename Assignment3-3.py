import numpy as np
from scipy import stats
import pandas as pd

# Simulated US Crime dataset (similar structure)
np.random.seed(42)
data = pd.DataFrame({
    "So": np.random.choice([0, 1], size=50),
    "Prob": np.random.normal(0.04, 0.01, size=50)
})

# Split groups
southern = data[data["So"] == 1]["Prob"]
nonsouthern = data[data["So"] == 0]["Prob"]

# Perform independent t-test
t_stat, p_val = stats.ttest_ind(southern, nonsouthern)

print("T-statistic:", t_stat)
print("P-value:", p_val)

# Hypothesis Discussion
if p_val < 0.05:
    print("✅ Reject Null Hypothesis: Significant difference between Southern and Non-Southern groups.")
else:
    print("❌ Fail to Reject Null Hypothesis: No significant difference between groups.")
