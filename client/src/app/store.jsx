import { configureStore } from '@reduxjs/toolkit';
import businessReducer from "../features/businesses/businessSlice"

export const store = configureStore({
  reducer: {
    businesses : businessReducer,
  },
});
