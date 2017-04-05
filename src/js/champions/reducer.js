const initialState = {
    /** 全てのチャンピオン */
    allChampions: [],
    /** 画面に描画すべきチャンピオン */
    champions: [],
}

const RENDER_ALL_CHAMPIONS = 'RENDER_ALL_CHAMPIONS'
const RENDER_PARTIAL_CHAMPIONS = 'RENDER_PARTIAL_CHAMPIONS'
const SEARCH_CHAMPIONS = 'SEARCH_CHAMPIONS'

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

export function searchChampions(keyword) {
    console.log(keyword)
    return {
        type: SEARCH_CHAMPIONS,
        data: {
            keyword: keyword
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
    case SEARCH_CHAMPIONS:
        // TODO ロジックがここにあるのはどうなのか
        var keyword = removeExceptKatakana(hiraganaToKatagana(action.data.keyword)).toLowerCase()
        var champions = state.allChampions
        if(keyword.length != 0) {
            console.log(keyword);
            champions = champions.filter((champion) => {
                if(champion.key.toLowerCase().indexOf(keyword) != -1) {
                    return true
                }
                if(removeExceptKatakana(champion.name).indexOf(keyword) != -1) {
                    return true
                }
                return false
            })
        }
        return Object.assign({}, state, {
            champions: champions
        })
    default:
        return state
    }
}

function hiraganaToKatagana(src) {
    return src.replace(/[\u3041-\u3096]/g, function(match) {
        var chr = match.charCodeAt(0) + 0x60;
        return String.fromCharCode(chr);
    });
}

function removeExceptKatakana(src) {
    return src.replace(/[^ァ-ンーA-Za-z]+/g, '')
}
