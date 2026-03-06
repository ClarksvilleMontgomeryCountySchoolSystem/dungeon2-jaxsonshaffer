bad = r"""
                        (  .      )
                      (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
good = r"""
_            _
 / \          / \
 |~|          |~|
#"'"|'"'"'"'"|"'"|
#   |  _.._  |   |
#   |.'    `.|   |
#   |        |   |
#   |.   /~~/~~/~~/
#   | './  /  /  /
#   |  /--/--/--/|
#   | /  /  /  / |
#   |/--/--/--/  |
#   |========#   | lbm
"""
guard_awake = True
if guard_awake:
    print(good)
    outcome = "Shadow: get through quick"
else:
    print(bad)
    oucome = "Doom: your a gonner"
print(outcome)
