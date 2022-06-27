local a = 'CiscoCTF{}'; 
local b = redis.call('get', 'key'); 
local c = 'MiScHiEVoUSHeDGEHoG'; 
redis.call('set', a, b:gsub('CiscoCTF{', ''):gsub('}', '') .. c:upper()); 
