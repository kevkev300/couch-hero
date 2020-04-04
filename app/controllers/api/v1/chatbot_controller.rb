class Api::V1::ChatbotController < Api::V1::BaseController
  def parse
    intent = intent_params
    parameters = parameter_params

    answer_text = find_answer(intent, parameters)
    @answer = Response.create(text: answer_text)

    render :response
  end

  def response
    @answer = Response.create(text: 'test')
    # render json: @answer
  end

  private

  def find_answer(intent, parameters)
    case intent
    when 'affected'
      `python3 lib/assets/python/test.py "#{parameters}"`
    end
  end

  def intent_params
    params.require[:intent].permit[:displayName]
  end

  def parameter_params
    params.require[:queryResult].permit[:parameters]
  end
end
