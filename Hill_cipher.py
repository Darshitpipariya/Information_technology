import numpy as np


def message(msg, dim):
    ms = []
    msg = msg.replace(' ', '')
    ind = 0
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = lower_alpha.upper()
    for index in range(0, len(msg), dim):
        messageVector = [[''] for i in range(dim)]
        for j in range(dim):
            if(index < len(msg)):
                if(msg[index].isupper()):
                    messageVector[j][0] = upper_alpha.index(msg[index])
                    index += 1
                else:
                    messageVector[j][0] = lower_alpha.index(msg[index])
                    index += 1
            else:
                messageVector[j][0] = ind
                ind += 1
                index += 1
        ms.append(messageVector)
    return ms


def key_matrix(key, dim):
    k_matrix = []
    k = key.replace(' ', '')
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = lower_alpha.upper()
    index = 0
    ind = 0
    for i in range(dim):
        l = []
        for j in range(dim):
            if(index < len(k)):
                if(k[index].isupper()):
                    l.append(upper_alpha.index(k[index]))
                    index += 1
                else:
                    l.append(lower_alpha.index(k[index]))
                    index += 1
            else:
                l.append(ind)
                ind += 1
        k_matrix.append(l)
    return k_matrix


def deter(k_matrix):
    a = np.array(k_matrix)
    return int(np.linalg.det(a))


def mat_mul(k_matrix, message_matrix):
    arr1 = np.array(k_matrix)
    arr2 = np.array(message_matrix)
    arr_result = np.matmul(arr1, arr2)
    arr_result = arr_result % 26




def Encryption():
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")
    dim=int(input("Enter dim"))
    k_m=key_matrix(key,dim)
    p_ve=message(plaintext,dim)
    cipher=[]
    for i in p_ve:
        cipher.append(mat_mul(k_m,i))