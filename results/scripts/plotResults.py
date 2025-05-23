import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data with proper pandas syntax
T_data = pd.read_csv('postProcessing/temperatureSampling/0.007/data_T.csv')
p_data = pd.read_csv('postProcessing/pressureSampling/0.007/data_p.csv')
U_data = pd.read_csv('postProcessing/velocitySampling/0.007/data_U.csv')

# Calculate velocity magnitude
U_data['magU'] = np.sqrt(U_data['U_0']**2 + U_data['U_1']**2 + U_data['U_2']**2)

# Create subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Temperature plot - fix pandas indexing
ax1.plot(T_data['x'].values, T_data['T'].values, 'r-', linewidth=2)
ax1.set_ylabel('Temperature (K)')
ax1.set_title('Temperature Distribution')
ax1.grid(True)

# Pressure plot
ax2.plot(p_data['x'].values, p_data['p'].values/1000, 'b-', linewidth=2)
ax2.set_ylabel('Pressure (kPa)')
ax2.set_title('Pressure Distribution')
ax2.grid(True)

# Velocity magnitude
ax3.plot(U_data['x'].values, U_data['magU'].values, 'g-', linewidth=2)
ax3.set_xlabel('Position (m)')
ax3.set_ylabel('Velocity Magnitude (m/s)')
ax3.set_title('Velocity Magnitude')
ax3.grid(True)

# All fields together (normalized)
T_max = T_data['T'].max()
p_max = p_data['p'].max()
U_max = U_data['magU'].max()

ax4.plot(T_data['x'].values, T_data['T'].values/T_max, 'r-', label='T (normalized)')
ax4.plot(p_data['x'].values, p_data['p'].values/p_max, 'b-', label='p (normalized)')
ax4.plot(U_data['x'].values, U_data['magU'].values/U_max, 'g-', label='|U| (normalized)')
ax4.set_xlabel('Position (m)')
ax4.set_ylabel('Normalized Values')
ax4.set_title('All Fields (Normalized)')
ax4.legend()
ax4.grid(True)

plt.tight_layout()
plt.savefig('shock_tube_results_pandas.png', dpi=300, bbox_inches='tight')
plt.show()
