require "json"
require "sinatra"

set :bind, "0.0.0.0"


get "/food" do
  content_type :json
  { answer: "yes" }.to_json
end