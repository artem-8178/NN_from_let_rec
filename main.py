import cv2
import numpy as np
import torch
import time
import torchvision.transforms as transforms
from torch.autograd import Variable


print("left-click = draw")
print("right-click = clean up")
print("scroll-wheel +/- = +/- brush size")

for i in range(0, 3):
    print(3 - i)
    time.sleep(0.5)

img = cv2.imread('t.png', 1)
img = cv2.resize(img, (480,480))
v_i = img.copy()
radius = 20
m_down = False

print("Load neural network")

net = torch.jit.load(r'bk_net_full_jitv2.pt')
net.eval()

print("Successful")

alf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def draw_circle(event, x, y, flags, param):
    global m_down
    global radius
    if event == cv2.EVENT_MOUSEMOVE and m_down == True:
        # print('(x:',x,',y:',y,')')
        # s_r = int(radius / 2 )
        # cv2.rectangle(img, (x - s_r, y - s_r), (x + s_r, y + s_r), (255,255,255), -1)
        cv2.circle(img, (x,y), radius, (255,255,255), -1)
    elif event == cv2.EVENT_LBUTTONDOWN:
        m_down = True
    elif event == cv2.EVENT_LBUTTONUP:
        m_down = False
    elif event == cv2.EVENT_RBUTTONDOWN:
        img[:,:] = 0
        print('Clear')
    elif event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            radius += 1
            # print(f"Radius +1 ({radius})")
        else:
            if radius < 1:
                return
            radius -= 1
            # print(f"Radius -1 ({radius})")
            
            
cv2.namedWindow('src')
cv2.setMouseCallback('src',draw_circle)

while(1):
    print('\n'*50)
    cv2.imshow('src',img)
    c_img = cv2.resize(img.copy(),(28,28))
    # tensor = torch.from_numpy(c_img)
    transform = transforms.ToTensor()
    tensor = transform(c_img)
    # print(tensor)
    tensor = Variable(tensor )
    tensor = tensor.view(-1, 28 * 28)
    rez = net(tensor)
    # print(rez)
    for i, b in enumerate(rez[0]):
        #print(i, b)
        print(f"{i + 1}  {alf[i]}  {b}")
    
    sd = rez[0].detach().numpy()
    max_ind = np.argmax(sd)
    print(f"brush size {radius}")
    print(f"This | {alf[max_ind]} |?")
    
    
    
    if cv2.waitKey (100) == ord ('q'): # Нажмите q, чтобы выйти
        break
cv2.destroyAllWindows()
