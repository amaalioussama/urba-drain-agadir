# app/routes/pompes.py
# Routes API pour les pompes

from flask import Blueprint, jsonify, request
from app.services import pompe_service
import os


def check_api_key():
    key = request.headers.get('X-API-Key', '')
    expected = os.getenv('SECRET_KEY', 'dev-secret-key-urba-drain-2026')
    return key == expected


bp = Blueprint('pompes', __name__)


@bp.route('', methods=['GET'])
def get_pompes():
    try:
        statut = request.args.get('statut')
        pompes = pompe_service.get_all_pompes(statut)
        return jsonify({
            'success': True,
            'count': len(pompes),
            'data': pompes
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:pompe_id>', methods=['GET'])
def get_pompe(pompe_id):
    try:
        pompe = pompe_service.get_pompe_by_id(pompe_id)
        if not pompe:
            return jsonify({'error': 'Pompe introuvable'}), 404
        return jsonify({
            'success': True,
            'data': pompe
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:pompe_id>/activer', methods=['POST'])
def activer_pompe(pompe_id):
    if not check_api_key():
        return jsonify({'error': 'Acces non autorise'}), 401
    try:
        data = request.get_json() or {}
        utilisateur = data.get('utilisateur')
        pompe = pompe_service.get_pompe_by_id(pompe_id)
        if not pompe:
            return jsonify({'error': 'Pompe introuvable'}), 404
        success = pompe_service.activer_pompe(pompe_id, utilisateur)
        if success:
            return jsonify({
                'success': True,
                'message': 'Pompe activated successfully'
            })
        else:
            return jsonify({'error': 'Activation failed'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:pompe_id>/desactiver', methods=['POST'])
def desactiver_pompe(pompe_id):
    if not check_api_key():
        return jsonify({'error': 'Acces non autorise'}), 401
    try:
        data = request.get_json() or {}
        utilisateur = data.get('utilisateur')
        pompe = pompe_service.get_pompe_by_id(pompe_id)
        if not pompe:
            return jsonify({'error': 'Pompe introuvable'}), 404
        success = pompe_service.desactiver_pompe(pompe_id, utilisateur)
        if success:
            return jsonify({
                'success': True,
                'message': 'Pompe deactivated successfully'
            })
        else:
            return jsonify({'error': 'Deactivation failed'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500