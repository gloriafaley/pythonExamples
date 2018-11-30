/*

Bob is making a video conference software. Whenever a new person joins the conference, Bob displays the person's name in the interface.

However, displaying full name is tedious and takes much space. So he decided to display the shortest prefix which doesn't match with any prefix of any person who has joined earlier.

Let's suppose the first person to enter the conference is alvin.

Now suppose next person to join is alice. The shortest prefix of alice that doesn't match with any prefix of alvin is ali.


Example - ('alvin', 'alice', 'alvin') 
For the first name 'alvin', 'a' prefix does not exist in the map, so that will be the displayed name 
Map - {a: 0, al: 0, alv: 0, alvi: 0, alvin: 1} 
For the second name 'alice', 'ali' prefix does not exist in the map 
Map - {a: 0, al: 0, alv: 0, alvi: 0, alvin: 1, ali: 0, alic: 0, alice: 1} 
For the last name 'alvin', the name already exists in the map, so 'alvin 2' will be the displayed name 
Map - {a: 0, al: 0, alv: 0, alvi: 0, alvin: 2, ali: 0, alic: 0, alice: 1}

If the full name of a new person matches completely with the full name of any person who has joined earlier,
he will display the full name and add a suffix which indicates how many times the same name has occurred in the list so far. 
For example, if another person name alvin joins, the list will look like this:

*/

n = int(input())
seen = {}
for _ in range(n):
    name = input().strip()
    l = len(name)
    this_done = False
    for x in range(1, l+1):
        cur_name = name[:x]
        if not this_done and cur_name not in seen:
            print(cur_name)
            this_done = True
        seen.setdefault(cur_name, 0)
    seen[name] += 1
    if not this_done and seen[name] == 1:
        print(name)
    elif not this_done:
        print('{} {}'.format(name, seen[name]))
