data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0:    # %是求餘數
		print(len(data)) #每讀一行列出來進度
print(len(data)) #讀取留言檔

print(data)  #印出data清單
print(data[0]) #印出第一筆留言
print('-------------------------------')
print(data[1]) #印出第二筆留言