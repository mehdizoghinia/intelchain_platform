import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import businessAPIService from "./businessAPIService";

const initialState = {
  businesses: [],
  business: {},
  isError: false,
  isLoading: false,
  isSuccess: false,
  message: "",
};

// get all Businesses
export const getBusinesses = createAsyncThunk(
  "business/getAll",
  async (_, thunkAPI) => {
    try {
      return await businessAPIService.getBusinesses();
    } catch (error) {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();

      return thunkAPI.rejectWithValue(message);
    }
  }
);

export const businessSlice = createSlice({
  name: "business",
  initialState,
  reducers: {
    reset: (state) => initialState,
  },
  extraReducers: (builder) => {
    builder
      .addCase(getBusinesses.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(getBusinesses.fulfilled, (state, action) => {
        state.isLoading = false;
        state.isSuccess = true;
        state.properties = action.payload.results;
      })
      .addCase(getBusinesses.rejected, (state, action) => {
        state.isLoading = false;
        state.isError = true;
        state.message = action.payload;
      });
  },
});

export const { reset } = businessSlice.actions;
export default businessSlice.reducer;
