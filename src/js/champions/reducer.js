const initialState = {
    /** 全てのチャンピオン */
    allChampions: [],
    /** 画面に描画すべきチャンピオン */
    champions: [],
}

const RENDER_ALL_CHAMPIONS = 'RENDER_ALL_CHAMPIONS'
const RENDER_PARTIAL_CHAMPIONS = 'RENDER_PARTIAL_CHAMPIONS'

/** 全部のチャンピオンを描画する（初期化処理的な） */
export function renderAllChampions(champions) {
    return {
        type: RENDER_ALL_CHAMPIONS,
        data: {
            champions: champions,
        }
    }
}

/** 一部のチャンピオンのみを描画する */
export function renderPartialChampions(champions) {
    return {
        type: RENDER_PARTIAL_CHAMPIONS,
        data: {
            champions: champions
        }
    }
}

export default function reducer(state = initialState, action) {
    switch(action.type) {
    case RENDER_ALL_CHAMPIONS:
        return Object.assign({}, state, {
            allChampions: action.data.champions,
            champions: action.data.champions,
        })
    case RENDER_PARTIAL_CHAMPIONS:
        return Object.assign({}, state, {
            champions: action.data.champions
        })
    default:
        return state
    }
}
