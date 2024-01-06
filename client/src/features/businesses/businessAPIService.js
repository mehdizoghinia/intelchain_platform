import axios from "axios";

//get properties
const getBusinesses = async () => {
  const response = await axios.get("/api/v1/businesses/");
  return response.data;
};

const businessAPIService = { getBusinesses };

export default businessAPIService;
