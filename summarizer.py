import requests

url = "https://api.meaningcloud.com/summarization-1.0"

string = "The band continued to explore a wider variation of musical types on their fourth album, A Thousand Suns (2010), layering their music with more electronic sounds. The band's fifth album, Living Things (2012), combined musical elements from all of their previous records. Their sixth album, The Hunting Party (2014), returned to a heavier rock sound, and their seventh album, One More Light (2017), was a substantially more pop-oriented record. Linkin Park went on a hiatus when longtime lead vocalist Bennington died in July 2017. In April 2022, Shinoda revealed the band was neither working on new music nor planning on touring for the foreseeable future."


payload={
    'key': '80af32ba0e3df9293b015185e9fc8120',
    'txt': string,
    'sentences': '1'
}

response = requests.post(url, data=payload, timeout=10)

print('Status code:', response.status_code)
print(response.json())