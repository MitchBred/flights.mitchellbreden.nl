from picamera2 import Picamera2
import boto3

picam2 = Picamera2()


def record(flightVideo):
    flight = str(flightVideo).lower().strip()
    picam2.start_and_record_video(flight, duration=10)
    upload_video(flight)


def upload_video(flight):
    client = boto3.client(
        's3',
        aws_access_key_id='AKIAVVEMZPXTG4GJY66G',
        aws_secret_access_key='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',
    )

    # image = 'images/flight.jpg'
    video = r'videos/' + flight
    client.upload_file(video, 'mitch-flights', flight)
