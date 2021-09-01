import {
    CREATE_BOOK,
    CREATE_BOOK_SUBMITTED,
    GET_BOOK_DETAIL,
    GET_BOOK_LIST,
    UPDATE_BOOK,
    UPDATE_BOOK_SUBMITTED,
    DELETE_BOOK,
    DELETE_BOOK_SUBMITTED
} from "./BookActionTypes.js";


const initialState = {
    books: []
};

export const bookReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_BOOK_LIST:
            return {
                ...state,
                books: [...state.notes, action.payload]
            };
        case CREATE_BOOK:
            return {
                ...state,
                books: [...state.notes, action.payload]
            };
        default:
            return state;
    }
};


