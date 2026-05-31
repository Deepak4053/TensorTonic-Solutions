def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    new_values = []
    for s in range(len(values)):
        best = float('-inf')
        for a in range(len(transitions[s])):
            q = rewards[s][a]
            for s_next in range(len(values)):
                q += gamma * transitions[s][a][s_next] * values[s_next]

            best = max(best, q)
        new_values.append(float(best))

    return new_values