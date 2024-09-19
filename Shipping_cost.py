weight = 5


#Envio terrestre
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $", cost_ground)

#Envio terrestre Premium
cost_ground_premium = 125.00

print("Ground Shipping Premium $", cost_ground_premium)

#Envio con drones
if weight <= 2:
  cost_drone = weight * 2.5 
elif weight <= 6:
  cost_drone = weight * 5.5
elif weight <= 10:
  cost_drone= weight * 7.5
else:
  cost_drone = weight * 8.5

print("Drone Shipping: $", cost_drone)

