from lazy_streams import stream

print(stream(['Gus', 'Joe', 'Sally', 'Mike', 'Jane']).reverse().to_list())