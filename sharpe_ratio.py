#sharpe ratio performance indicator
s=0.061
if s<0:
    print('underperforming')
elif s<1:
    print('suboptimal')
elif s<2:
    print('good')
else:
    print('elite')
print('complete')
