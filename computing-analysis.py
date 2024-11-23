import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
num_requests = 1000  # Total number of requests
complex_task_ratio = 0.6  # Percentage of requests that are computationally intensive

# Cloud parameters
cloud_latency = np.random.normal(200, 20, num_requests)
cloud_processing_time = np.random.normal(50, 10, num_requests)
cloud_total_time = cloud_latency + cloud_processing_time

# Edge parameters
edge_latency = np.random.normal(10, 5, num_requests)
edge_processing_time_simple = np.random.normal(15, 5, int(num_requests * (1 - complex_task_ratio)))
edge_processing_time_complex = np.random.normal(100, 20, int(num_requests * complex_task_ratio))
edge_total_time = np.concatenate((edge_latency[:len(edge_processing_time_simple)] + edge_processing_time_simple,
                                   edge_latency[len(edge_processing_time_simple):] + edge_processing_time_complex))

# Fog parameters
fog_latency = np.random.normal(50, 10, num_requests)
fog_processing_time_simple = np.random.normal(20, 5, int(num_requests * (1 - complex_task_ratio)))
fog_processing_time_complex = np.random.normal(40, 10, int(num_requests * complex_task_ratio))
fog_total_time = np.concatenate((fog_latency[:len(fog_processing_time_simple)] + fog_processing_time_simple,
                                  fog_latency[len(fog_processing_time_simple):] + fog_processing_time_complex))

# Critical threshold
critical_processing_threshold = 100

# Calculate percentages of requests meeting the threshold
cloud_meeting_threshold = np.sum(cloud_total_time <= critical_processing_threshold) / num_requests * 100
edge_meeting_threshold = np.sum(edge_total_time <= critical_processing_threshold) / num_requests * 100
fog_meeting_threshold = np.sum(fog_total_time <= critical_processing_threshold) / num_requests * 100

# Visualization
plt.figure(figsize=(12, 6))
plt.hist(cloud_total_time, bins=30, alpha=0.7, label=f'Cloud-Only (Met Threshold: {cloud_meeting_threshold:.2f}%)', color='blue')
plt.hist(edge_total_time, bins=30, alpha=0.7, label=f'Edge-Only (Met Threshold: {edge_meeting_threshold:.2f}%)', color='orange')
plt.hist(fog_total_time, bins=30, alpha=0.7, label=f'Fog-Only (Met Threshold: {fog_meeting_threshold:.2f}%)', color='green')

plt.axvline(critical_processing_threshold, color='red', linestyle='dashed', linewidth=1.5, label=f'Critical Threshold: {critical_processing_threshold}ms')

# Add average lines
plt.axvline(np.mean(cloud_total_time), color='blue', linestyle='dotted', linewidth=1.5, label=f'Cloud Avg: {np.mean(cloud_total_time):.2f}ms')
plt.axvline(np.mean(edge_total_time), color='orange', linestyle='dotted', linewidth=1.5, label=f'Edge Avg: {np.mean(edge_total_time):.2f}ms')
plt.axvline(np.mean(fog_total_time), color='green', linestyle='dotted', linewidth=1.5, label=f'Fog Avg: {np.mean(fog_total_time):.2f}ms')

# Plot settings
plt.title('Performance Comparison: Cloud vs Edge vs Fog (Including Complexity)')
plt.xlabel('Total Processing Time (ms)')
plt.ylabel('Number of Requests')
plt.legend()
plt.grid()
plt.show()

# Summary of results
print("Performance Summary:")
print(f"Cloud-Only: {cloud_meeting_threshold:.2f}% requests met the critical threshold.")
print(f"Edge-Only: {edge_meeting_threshold:.2f}% requests met the critical threshold.")
print(f"Fog-Only: {fog_meeting_threshold:.2f}% requests met the critical threshold.")