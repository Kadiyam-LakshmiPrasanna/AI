P_D = 0.2
P_not_D = 0.8
P_F_given_D = 0.8
P_F_given_not_D = 0.1
P_F = (P_F_given_D * P_D) +(P_F_given_not_D * P_not_D)
P_D_given_F = (P_F_given_D * P_D)/P_F
print("P(Fever) = ",P_F)
print("P(Disease)|Fever) = ",round(P_D_given_F,2))
