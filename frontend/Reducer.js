import { combineReducers } from "redux";
import { connectRouter } from "connected-react-router";

import { bookReducer } from "./components/books/BookReducer";

const createRootReducer = history =>
    combineReducers({
        router: connectRouter(history),
        books: bookReducer
    });