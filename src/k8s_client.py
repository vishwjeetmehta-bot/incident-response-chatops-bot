def diagnose_failing_pods(namespace: str = "production") -> str:
    """Mock/Real Kubernetes diagnosis fetching CrashLoopBackOff pods and tailing logs."""
    return (
        f"[Target Namespace: {namespace}]\n"
        f"Found 1 Pod in CrashLoopBackOff: payment-service-7bb85-x29f\n"
        f"Exit Code: 137 (OOMKilled)\n"
        f"Memory Limit: 256Mi | Peak Usage: 260Mi\n"
        f"Suggested Action: Scale memory limit to 512Mi or trigger runbook '/sre remediate-oom payment-service'"
    )
