require 'yaml'

Dir.glob('_categories/*.md') do |file|
  describe "Category page: " + file do
  
    unless file == '_categories/all_links.md'
      category = YAML.load_file(file)
      it "has a non-empty title" do
        expect(category).to have_key("title")
        expect(category["title"]).not_to eq("")
      end

      it "has a non-empty description" do
        expect(category).to have_key("desc")
        expect(category["desc"]).not_to eq("")
      end

      it "has subcategories" do
        expect(category).to have_key("subcategories")
        expect(category["subcategories"].length).to be > 0
      end
      
      category["subcategories"].each_with_index { |subcat, s_index|
        describe "Subcategory #" + s_index.to_s + ": " + subcat["title"] do
          it "has a non-empty title" do
            expect(category["subcategories"][0]).to have_key("title")
            expect(category["subcategories"][0]["title"]).not_to eq("")
          end
          
          it "has index items" do
            expect(subcat).to have_key("items")
            expect(subcat["items"].length).to be > 0
          end

          subcat["items"].each_with_index { |item, i_index|
            describe "Index item #" + i_index.to_s + " :" + item["title"] do
              it "has non-empty title" do
                expect(item).to have_key("title")
                expect(item["title"]).not_to eq("")
              end
              
              it "has a non-empty url" do
                expect(item).to have_key("url")
                expect(item["url"]).not_to eq("")
              end
              
              it "has a non-empty description" do
                expect(item).to have_key("desc")
                expect(item["desc"]).not_to eq("")
              end
              
              it "has a star boolean" do
                expect(item).to have_key("star")
                expect(item["star"]).to be(true).or be(false)
              end            
            end
          }

        end
      }

    end
  end
end