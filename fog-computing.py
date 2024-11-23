import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
num_requests = 1000  # Total number of requests
fog_processing_ratio = 0.7  # % of requests handled by fog nodes in fog-enabled system
cloud_latency = np.random.normal(200, 20, num_requests)  # Cloud latency in ms
cloud_processing_time = np.random.normal(50, 10, num_requests)  # Cloud processing time in ms
fog_latency = np.random.normal(50, 10, num_requests)  # Fog latency in ms
fog_processing_time = np.random.normal(10, 5, num_requests)  # Fog processing time in ms

# Cloud-only infrastructure total time (latency + processing time)
cloud_only_total_time = cloud_latency + cloud_processing_time

# Fog-enabled infrastructure total time
fog_processed = fog_latency[:int(num_requests * fog_processing_ratio)] + fog_processing_time[:int(num_requests * fog_processing_ratio)]
cloud_processed = cloud_latency[int(num_requests * fog_processing_ratio):] + cloud_processing_time[int(num_requests * fog_processing_ratio):]
fog_enabled_total_time = np.concatenate((fog_processed, cloud_processed))

# Average processing time comparison
cloud_only_avg_time = np.mean(cloud_only_total_time)
fog_enabled_avg_time = np.mean(fog_enabled_total_time)

# Visualization
plt.figure(figsize=(10, 6))
plt.hist(cloud_only_total_time, bins=30, alpha=0.7, label='Cloud-Only Infrastructure', color='blue')
plt.hist(fog_enabled_total_time, bins=30, alpha=0.7, label='Fog-Enabled Infrastructure', color='green')
plt.axvline(cloud_only_avg_time, color='blue', linestyle='dashed', linewidth=1.5, label=f'Cloud Avg Time: {cloud_only_avg_time:.2f}ms')
plt.axvline(fog_enabled_avg_time, color='green', linestyle='dashed', linewidth=1.5, label=f'Fog Avg Time: {fog_enabled_avg_time:.2f}ms')
plt.title('Performance Comparison: Cloud-Only vs Fog-Enabled Infrastructure')
plt.xlabel('Total Processing Time (ms)')
plt.ylabel('Number of Requests')
plt.legend()
plt.grid()
plt.show()