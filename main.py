#Quadratic equation solver
print("Welcome to QE solver")
print("\nPlease, insert coefficient for ax^2")
coef_a = int(input())
print("\nPlease, insert coefficient for bx")
coef_b = int(input())
print("\nPlease, insert coefficient for c")
coef_c = int(input())

discriminant = coef_b**2 - (4 * coef_a * coef_c)
root_x1 = (coef_b*(-1)+discriminant**(1/2))/(2*coef_a)
root_x2 = (coef_b*(-1)-discriminant**(1/2))/(2*coef_a)

if discriminant < 0:
    print("\nNo real solutions")
elif discriminant == 0:
    print("\nQE has one real solution")
    print("x = " + str(root_x1))
else:
    print("\nRoots for QE are:")
    print("x_1 = " + str(root_x1))
    print("\nx_2 = " + str(root_x2))
