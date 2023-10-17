#region debai
"""
--- ma debai / id
greeting(hour_str)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310171122greetinghourstr

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/mb6ZrFw4pXW8DqeBA

--- debai / problem
Viết hàm 
  greeting(hour_str)
giúp chat bot in ra câu chào theo buổi sáng/chiều/tối trong ngày 
00:00AM  - 11:59AM Good morning!
12:00PM  - 05:59PM Good afternoon!
06:00PM  - 11:59PM Good evening!

Khi chạy với đầuvào / input  | Kếtquả đẩura / output  | Thứtự mẫuthử 
---------------------------- | ---------------------- | -----------
greeting(hour_str='6am')     | Good morning!          | 00

# AM / PM format
greeting('6am')              | Good morning!          | 01
greeting('6 am')             | Good morning!          | 02
greeting('6AM')              | Good morning!          | 03
greeting('6 AM')             | Good morning!          | 04

greeting('9pm')              | Good evening!          | 05
greeting('0900pm')           | Good evening!          | 06
greeting('09:00pm')          | Good evening!          | 07
greeting('09:00 pm')         | Good evening!          | 08
greeting('09:00 PM')         | Good evening!          | 09

greeting('1pm')              | Good afternoon!        | 10

# 24-hours format
greeting('06:00')            | Good morning!          | 11
greeting('0600')             | Good morning!          | 12
greeting('21:00')            | Good evening!          | 13
greeting('2100')             | Good evening!          | 14

"""
#endregion debai
def greeting(hour_str):
  hour_str=hour_str.replace(':','')
  hour_str=hour_str.replace(' ','')
  hour_str=hour_str.lower()
  hour=''
  min=''
  if hour_str.find('am') >= 0 or hour_str.find('pm') >= 0:
      len_report=len(hour_str) - 2
  else:
      len_report=len(hour_str)

  if len_report < 4:
      if hour_str.find('am') >= 0:
          hour=hour_str[0]
          min='00'
      elif hour_str.find('pm') >= 0:
          hour=str(int(hour_str[0])+12)
          min='00'
  elif len_report >= 4:
      for i in range(0,len_report):
          if i <= 1:
              hour+=hour_str[i]
          elif i > 1 and i <= 3:
              min+=hour_str[i]
      if hour_str.find('pm') >= 0:
          hour=str(int(hour)+12)

  if int(hour) >= 0 and int(hour) <= 11 and int(min) <= 59:
      return 'Good morning!'
  elif int(hour) >= 12 and int(hour) <= 17 and int(min) <= 59:
      return 'Good afternoon!'
  elif int(hour) >= 18 and int(hour) <= 23 and int(min) <= 59:
      return 'Good evening!'
#region bailam

#endregion bailam
