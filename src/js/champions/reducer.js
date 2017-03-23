const initialState = {
    champions: []
}

const RENDER_CHAMPIONS = 'RENDER_CHAMPIONS'

export function renderChampions(champions) {
    return {
        type: RENDER_CHAMPIONS,
        data: champions
    }
}

export default function reducer(state = initialState, action) {
    switch(action.type) {
    case RENDER_CHAMPIONS:
        return Object.assign({}, state, {
            champions: action.data
        })
    default:
        return state
    }
}
