graph [
directed 1
version 2
node [
    id 0
    label ""
    graphics [
        x 0
        y -93
        z 0
        h 182
        w 186
        d 0
        type "rectangle"
        width 0.12
        fill "#ff0000"
        outline "#000000"
     ]
]
node [
id 1
label ""
graphics [
x 0
y -331.5
z 0
h 40
w 91
d 0
type "rectangle"
width 0.12
fill "#ff0000"
outline "#000000"
     ]
]
node [
id 2
label ""
graphics [
x -150
y -527
z 0
h 100
w 100
d 0
type "rectangle"
width 0.12
fill "#ff0000"
outline "#000000"
     ]
]
node [
id 3
label ""
graphics [
x 0
y -527
z 0
h 100
w 100
d 0
type "rectangle"
width 0.12
fill "#ff0000"
outline "#000000"
     ]
]
node [
id 4
label ""
graphics [
x 150
y -527
z 0
h 100
w 100
d 0
type "rectangle"
width 0.12
fill "#ff0000"
outline "#000000"
     ]
]
edge [
source 0
target 1
id 0
label ""
graphics [
type "line"
arrow "last"
width 0.1
Line [
]
]
]
edge [
    source 1
    target 2
    id 1
    label ""
    graphics [
        type "line"
        arrow "last"
        width 0.1
        Line [
            point [
                x 0
                y -331.5
                z 0
            ]
            point [
                x -150
                y -331.5
                z 0
            ]
            point [
                x -150
                y -527
                z 0
            ]
        ]
    ]
]
edge [
source 1
target 3
id 2
label ""
graphics [
type "line"
arrow "last"
width 0.1
Line [
]
]
]
edge [
source 1
target 4
id 3
label ""
graphics [
type "line"
arrow "last"
width 0.1
Line [
point [
x 0
y -331.5
z 0
]
point [
x 150
y -331.5
z 0
]
point [
x 150
y -527
z 0
]
]
]
]
]
