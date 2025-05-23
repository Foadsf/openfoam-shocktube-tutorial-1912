import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

# Read CSV data manually
def read_csv_data(filename):
    data = np.loadtxt(filename, delimiter=',', skiprows=1)
    return data

# Read data
T_data = read_csv_data('postProcessing/temperatureSampling/0.007/data_T.csv')
p_data = read_csv_data('postProcessing/pressureSampling/0.007/data_p.csv')
U_data = read_csv_data('postProcessing/velocitySampling/0.007/data_U.csv')

# Calculate velocity magnitude
magU = np.sqrt(U_data[:,1]**2 + U_data[:,2]**2 + U_data[:,3]**2)

# Create plots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Temperature
ax1.plot(T_data[:,0], T_data[:,1], 'r-', linewidth=2)
ax1.set_ylabel('Temperature (K)')
ax1.set_title('Temperature Distribution')
ax1.grid(True)

# Pressure
ax2.plot(p_data[:,0], p_data[:,1]/1000, 'b-', linewidth=2)
ax2.set_ylabel('Pressure (kPa)')
ax2.set_title('Pressure Distribution')
ax2.grid(True)

# Velocity magnitude
ax3.plot(U_data[:,0], magU, 'g-', linewidth=2)
ax3.set_xlabel('Position (m)')
ax3.set_ylabel('Velocity Magnitude (m/s)')
ax3.set_title('Velocity Magnitude')
ax3.grid(True)

# Combined
ax4.plot(T_data[:,0], T_data[:,1]/np.max(T_data[:,1]), 'r-', label='T (norm)')
ax4.plot(p_data[:,0], p_data[:,1]/np.max(p_data[:,1]), 'b-', label='p (norm)')
ax4.plot(U_data[:,0], magU/np.max(magU), 'g-', label='|U| (norm)')
ax4.set_xlabel('Position (m)')
ax4.set_ylabel('Normalized Values')
ax4.set_title('All Fields (Normalized)')
ax4.legend()
ax4.grid(True)

plt.tight_layout()
plt.savefig('shock_tube_results.png', dpi=300, bbox_inches='tight')
print("Plot saved as 'shock_tube_results.png'")
