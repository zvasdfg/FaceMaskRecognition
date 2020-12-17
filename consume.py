import urllib.request, json

def consume(mask):
    if (mask == 'mask'):
        url = "http://ec2-3-19-222-142.us-east-2.compute.amazonaws.com/mask"
    elif (mask == 'noMask'):
        url = "http://ec2-3-19-222-142.us-east-2.compute.amazonaws.com/noMask"
    else:
        url = "http://ec2-3-19-222-142.us-east-2.compute.amazonaws.com/noMask"
    response = urllib.request.urlopen(url)
    data = response.read()

    return (data)

