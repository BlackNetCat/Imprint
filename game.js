const textElement = document.getElementById('text')
const optionButtonsElement = document.getElementById('option-buttons')

let state = {}

function startGame() {
  state = {}
  showTextNode(1)
}

function showTextNode(textNodeIndex) {
  const textNode = textNodes.find(textNode => textNode.id === textNodeIndex)
  textElement.innerText = textNode.text
  while (optionButtonsElement.firstChild) {
    optionButtonsElement.removeChild(optionButtonsElement.firstChild)
  }
  textNode.options.forEach(option => {
    if (showOption(option)) {
      const button = document.createElement('button')
      button.innerText = option.text
      button.classList.add('btn')
      button.addEventListener('click', () => selectOption(option))
      optionButtonsElement.appendChild(button)
    }
  })
}

function showOption(option) {
  return option.requiredState == null || option.requiredState(state)
}

function selectOption(option) {
  const nextTextNodeId = option.nextText
  if (nextTextNodeId <= 0) {
    return startGame()
  }
  state = Object.assign(state, option.setState)
  showTextNode(nextTextNodeId)
}

const textNodes = [
  {
    id: 1,
    text: 'fight in Past Tense?',
    options: [
      {
        text: 'foreght',
       // setState: { blueGoo: true},
        nextText: 5
      },
      {
        text: 'fought',       
        nextText: 2
      },
      {
        text: 'fight',
      //  setState: { blueGoo: true},
        nextText: 5
      },
      {
        text: 'fuck',
     //   setState: { blueGoo: true},
        nextText: 5
      },
      
    ]
  },
  {
    id: 2,
    text: 'Begin in Past Participle',
    options: [
      {
        text: 'begun',
        //requiredState: (currentState) => currentState.blueGoo,
       // setState: {blueGoo: false, sword: true},
        nextText: 5
      },
      {
        text: 'began',
       // requiredState: (currentState) => currentState.blueGoo,
       // setState: {blueGoo: false, shield: true},
        nextText: 3
      },
      {
        text: 'begin',
       // requiredState: (currentState) => currentState.blueGoo,
       // setState: {blueGoo: false, sword: true},
        nextText: 5
      },
      {
        text: 'begen',
        nextText: 5
      }
    ]
    
  },
  {
    id: 3,
    text: 'Freeze in Past Tense',
    options: [
      {
        text: 'frozen',
        nextText: 5
      },
      {
        text: 'freeze',
        nextText: 5
      },
      {
        text: 'froze',
        nextText: 4
      },
      {
        text: 'freezen',
        nextText: 5
      }    

    ]
  },
  {
    id: 4,
    text: 'Grow in Past Participle',
    options: [
      {
        text: 'grow',
        nextText: 5
      },
      {
        text: 'grew',
        nextText: 5
      },
      {
        text: 'geen',
        nextText: 4
      },
      {
        text: 'grown',
        nextText: 100
      }    

    ]
  },
  {
    id: 5,
    text: 'Не верно, попробуйте еще',
    options: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]

  },
  {
    id: 100,
    text: 'Победа',
    options: [
      {
        text: 'Restart',
        nextText: -1
      }
    ]

  }
]

startGame()