    # To run this, download the BeautifulSoup zip file
    # http://www.py4e.com/code3/bs4.zip
    # and unzip it in the same directory as this file

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import ssl

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('span')
    num1 = []
    for tag in tags:
        # Look at the parts of a tag
        # print('TAG:', tag)
        num1.append(int(tag.text))
        # print('Contents:', tag.contents[0])
        # print('Attrs:', tag.attrs)

    print(num1)
    sum = 0

    for item in num1:
        sum += item

    print(sum)
