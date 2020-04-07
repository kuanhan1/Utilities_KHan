# expand local patch
a = torch.arange(40).reshape([1,2,4,5])
def patch_expand(a, kernel_size=3, padding=1):
    # a_pad = F.pad(a,(padding,padding,padding,padding),"constant", 0)
    b=F.unfold(F.pad(a,(padding,padding,padding,padding),"constant", 0).float(), kernel_size = (kernel_size,kernel_size))
    c=F.fold(b, output_size=(a.shape[2]*3, a.shape[3]*3),kernel_size=(kernel_size,kernel_size), stride=kernel_size)
    return c
