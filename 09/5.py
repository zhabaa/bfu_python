import numpy as np

def log_multivariate_normal_pdf(X, m, C):
    D = m.size
    diff = X - m
    inv_C = np.linalg.inv(C)
    det_C = np.linalg.det(C)
    
    log_pdf = -0.5 * (D * np.log(2 * np.pi) + np.log(det_C) + np.sum(diff @ inv_C * diff, axis=1))
    return log_pdf

X = np.random.randn(100, 3)
m = np.zeros(3)
C = np.eye(3)

logpdf = log_multivariate_normal_pdf(X, m, C)
print("Логарифм плотности для первых 5 точек:", logpdf[:5])
