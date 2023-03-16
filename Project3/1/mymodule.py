import numpy as np

def handler(input,context):
    output = {}
    n_cpu = 12
    cpu = ["CPU"+str(i) for i in range(n_cpu)]
    cpu_res = [0 for _ in range(n_cpu)]
    for i in range(n_cpu):
        i_cpu = context.env.get(i,[])
        cpu_percent_i = input["cpu_percent-"+str(i)]
        i_cpu.append(cpu_percent_i)
        n_cpu_i = len(i_cpu)
        if n_cpu_i > 12:
            i_cpu.pop(0)
        context.env[i] = i_cpu
        cpu_res[i] = np.round(np.mean(i_cpu),3)
    output["CPU"] = [cpu,cpu_res]
    
    buffers = context.env.get("buffers",[])
    buffers_temp = input["virtual_memory-buffers"]
    n_buffers = len(buffers)
    buffers.append(buffers_temp)
    cached = context.env.get("cached",[])
    cached_temp = len(cached)
    cached.append(cached_temp)
    n_cached = len(cached)
    if n_buffers > 12:
        buffers.pop(0)
    if n_cached > 12:
        cached.pop(0)
    context.env["buffers"] = buffers
    context.env["cached"] = cached
    output["buffers"] = np.round(np.mean(buffers),3)
    output["cached"] = np.round(np.mean(cached),3)
    return output

