import axios from "axios";
// import { toastOnError } from "../../utils/Utils";

import {
    CREATE_BOOK,
    // CREATE_BOOK_SUBMITTED,
    // GET_BOOK_DETAIL,
    GET_BOOK_LIST,
    // UPDATE_BOOK,
    // UPDATE_BOOK_SUBMITTED,
    // DELETE_BOOK,
    // DELETE_BOOK_SUBMITTED
} from "./BookActionTypes.js";


export const getBooks = () => dispatch => {
    axios
        .get("/api/v1/books")
        .then(response => {
            dispatch({
                type: GET_BOOK_LIST,
                payload: response.data
            });
        })
        /*
        .catch(error => {
            toastOnError(error);
        });
        */
};

export const createBook = book => dispatch => {
    axios
        .post("/api/v1/books", book)
        .then(response => {
            dispatch({
                type: CREATE_BOOK,
                payload: response.data
            });
        })
        /*
        .catch(error => {
            toastOnError(error);
        });
        */
};